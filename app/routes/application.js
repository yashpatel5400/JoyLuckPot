import Ember from 'ember';

export default Ember.Route.extend({
  model() {
    this.store.findAll('event');
    this.store.findAll('user');
    this.store.findAll('attendee');
  }
});
