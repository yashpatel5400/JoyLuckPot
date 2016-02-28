import Ember from 'ember';

export default Ember.Controller.extend({
  openJoinModal: false,
  actions: {
    join() {
      this.set("openJoinModal", true);
    }
  }
});
