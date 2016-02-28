import Ember from 'ember';

export default Ember.Controller.extend({
  userLocation: null,
  userLat: 0,
  userLng: 0,
  onLocationUpdate: function () {
    var loc = this.get("userLocation");
    this.set("userLat", loc.coords.latitude);
    this.set("userLng", loc.coords.longitude);

    $('.map-location-overlay h1').html('<i class="fa fa-thumbs-o-up"></i>');
    $('.map-location-overlay').addClass('approved');
    setTimeout(function () {
        $('.map-location-overlay').css('zIndex', '-1')
    }, 1200);
  }.observes("userLocation"),
  filterFriends: true,
  filterPublic: true,
  filterDistance: 20,
  filterDate: 7,

    openCreateModal: false,
  actions: {
    create() {
      this.set("openCreateModal", true);
    }
  }
});
