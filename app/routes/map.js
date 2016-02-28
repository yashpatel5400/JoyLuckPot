import Ember from 'ember';

export default Ember.Route.extend({
  geolocation: Ember.inject.service(),
  setupController: function (controller, model) {
    this._super(controller, model);
    this.get('geolocation').getLocation().then(function (geoObject) {
      controller.set('userLocation', geoObject);
    });
  },
  model() {
    return this.store.findAll("event");
  }
});
