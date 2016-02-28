import Ember from 'ember';

export default Ember.Route.extend({
  model(params) {
  	return Ember.RSVP.hash({
    	event: this.store.peekRecord('event', params.event_id)
  	});
  }
});
