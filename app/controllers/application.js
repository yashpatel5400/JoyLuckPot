import Ember from 'ember';

export default Ember.Controller.extend({
  userName: function () {
    return this.get("user.name");
  }.property("user")
});
