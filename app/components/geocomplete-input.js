import Ember from 'ember';

export default Ember.Component.extend({
  didInsertElement() {
    this.$(".geocomplete").geocomplete({
      map: this.$('.map-canvas'),
      markerOptions: {
        draggable: true
      }
    });

    this.$(".geocomplete").bind("geocode:result", (event, result) => {
      var latLng = result.geometry.location;
      this.set("lat", latLng.lat());
      this.set("lng", latLng.lng());
    });

    this.$(".geocomplete").bind("geocode:dragged", (event, latLng) => {
      this.set("lat", latLng.lat());
      this.set("lng", latLng.lng());
    });
  }
});
