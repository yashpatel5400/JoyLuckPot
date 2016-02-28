import Ember from 'ember';

export default Ember.Component.extend({
  foods: null,
  fToI: null,
  didInsertElement() {
    var userId = this.get("user.id");
    var eventId = this.get("event.id");
    var _this = this;
    Ember.$.getJSON('/suggestions', {"user_id": userId, "event_id": eventId}, function (data) {
      var s = data.suggestions;
      var foods = s[0];
      var images = s[1];
      var fToI = [];
      for (var i = 0; i < foods.length; i++) {
        fToI.push({food: foods[i], images: images[i]});
      }
      _this.set("foods", foods);
      _this.set("fToI", fToI);
    });
  }
});
