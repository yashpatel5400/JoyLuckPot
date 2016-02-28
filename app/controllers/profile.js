import Ember from 'ember';

export default Ember.Controller.extend({
  selected: function () {
    return this.get("application.user.preferences").split(",");
  }.property("application.user.preferences"),
  application: Ember.inject.controller(),
  actions: {
    save() {
      this.set("application.user.preferences", this.get("selected").join(","));
      this.get("application.user").save();
      this.transitionToRoute("map");
    }
  }
});
