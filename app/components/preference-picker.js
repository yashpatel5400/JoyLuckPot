import Ember from 'ember';

export default Ember.Component.extend({
  svg: null,
  nodes: [],
  force: null,

  init() {
    this._super(...arguments);
    this.get('resizeService').on('didResize', e => {
      this.send("doResize");
    });
  },

  actions: {
    doResize() {
      var width = this.$("svg").width();
      var height = this.$("svg").height();
      this.get("force").size([width, height]).resume();
    },
    explode() {
      this.get("force").friction(1).gravity(0).charge(-5000).start();
    },
    findMore() {
      var nodes = this.get("nodes");
      console.log(nodes);

      for (var i = nodes.length - 1; i >= 0; i--) {
        if (!nodes[i].isSelected) nodes.splice(i, 1);
      }

      this.send("_updateNodes");

      setTimeout(() => {
        this.send("_addNodes");
        this.send("_updateNodes");
      }, 0);
    },
    _addNodes() {
      var nodes = this.get("nodes");

      var currentWords = nodes.map(function (n) { return n.text; });
      var allShuffledWords = d3.shuffle(window.FOOD_WORDS);

      var minRadius = 50,
          maxRadius = 70,
          n = 20 - nodes.length,
          i = 0;

      d3.range(n).map(function() {
        while (currentWords.indexOf(allShuffledWords[i]) != -1) i++;
        currentWords.push(allShuffledWords[i]);
        var r = Math.random() * (maxRadius - minRadius) + minRadius;
        nodes.push({radius: r, text: allShuffledWords[i], isSelected: false});
        i++;
      });
    },
    _updateNodes() {
      var svg = this.get("svg");
      var force = this.get("force");
      var nodes = this.get("nodes");

      var nodesUpdate = svg.selectAll("g")
          .data(nodes, function(d) { return d.text; });

      var nodesEnter = nodesUpdate
          .enter()
          .append("g")
          .style("cursor", "pointer")
          .on("click", function (d) {
            d.isSelected = !d.isSelected;
            d.radius = d.isSelected ? d.radius * 1.2 : d.radius / 1.2;
            d3.select(this)
                .attr("d", d)
                .select("circle")
                    .attr("r", d.radius)
                    .style("fill", d.isSelected ? "red" : "pink");
            force.resume();
          });

      nodesEnter.append("circle")
          .attr("r", function(d) { return d.radius; })
          .style("fill", "pink")
          .style("transition", "fill 0.2s, r 0.2s");

      var sqrt2 = Math.sqrt(2);

      nodesEnter.append("foreignObject")
          .attr("x", function (d) { return -d.radius / sqrt2; })
          .attr("y", function (d) { return -d.radius / sqrt2; })
          .attr("width", function (d) { return d.radius * sqrt2; })
          .attr("height", function (d) { return d.radius * sqrt2; })
          .style("overflow", "hidden")
          .append("xhtml:div")
              .text(function (d) { return d.text; })
              .style("color", "white")
              .style("text-align", "center")
              .style("height", "100%")
              .style("display", "flex")
              .style("justify-content", "center")
              .style("align-items", "center")
              .style("word-wrap", "break-word");

      nodesUpdate.exit().remove();

      force.start();
    }
  },

  didInsertElement() {
    this.$().css({width: "100%", height: "100%"});

    var width = 960,
        height = 500,
        padding = 5,
        minRadius = 40,
        maxRadius = 50;

    var n = 30; // total number of circles

    // var nodes = d3.range(n).map(function() {
    //   var r = Math.random() * (maxRadius - minRadius) + minRadius;
    //   return {radius: r, text: "" + r, isSelected: false};
    // });
    // this.set("nodes", nodes);
    this.set("nodes", []);
    this.send("_addNodes");
    var nodes = this.get("nodes");
    setTimeout(() => this.send("_updateNodes"), 0);

    var force = d3.layout.force()
        .nodes(nodes)
        .size([width, height])
        .charge(0)
        .friction(0.5)
        .on("tick", tick)
        .start();
    this.set("force", force);
    setTimeout(() => this.send("doResize"), 0);

    var svg = d3.select(this.$().get(0)).append("svg")
        // .attr("width", width)
        // .attr("height", height);
        .style("width", "100%")
        .style("height", "100%");
    this.set("svg", svg);

    function tick(e) {
      svg.selectAll("g")
          .each(collide(.5))
          .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
    }

    // Resolves collisions between d and all other circles.
    function collide(alpha) {
      var quadtree = d3.geom.quadtree(nodes);
      return function(d) {
        var r = d.radius + maxRadius + padding,
            nx1 = d.x - r,
            nx2 = d.x + r,
            ny1 = d.y - r,
            ny2 = d.y + r;
        quadtree.visit(function(quad, x1, y1, x2, y2) {
          if (quad.point && (quad.point !== d)) {
            var x = d.x - quad.point.x,
                y = d.y - quad.point.y,
                l = Math.sqrt(x * x + y * y),
                r = d.radius + quad.point.radius + padding;
            if (l < r) {
              l = (l - r) / l * alpha;
              d.x -= x *= l;
              d.y -= y *= l;
              quad.point.x += x;
              quad.point.y += y;
            }
          }
          return x1 > nx2 || x2 < nx1 || y1 > ny2 || y2 < ny1;
        });
      };
    }
  }
});
