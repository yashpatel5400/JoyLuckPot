import Ember from 'ember';

export default Ember.Controller.extend({


  userLocation: null,
  onLocationUpdate: function () {
    var loc = this.get("userLocation");

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
  },

});
