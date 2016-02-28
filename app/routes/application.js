import Ember from 'ember';

export default Ember.Route.extend({
  model() {
    // Wait to preload all data
    return Ember.RSVP.all([
      this.store.findAll('event'),
      this.store.findAll('user'),
      this.store.findAll('attendee')
    ]);
  }
});
