import Ember from 'ember';

export default Ember.Controller.extend({
  application: Ember.inject.controller(),
  openJoinModal: false,
  actions: {
    join() {
      this.set("openJoinModal", true);
    }
  }
});
