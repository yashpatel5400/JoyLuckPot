import Ember from 'ember';

export default Ember.Controller.extend({
  application: Ember.inject.controller(),
  //fbData: null,
  ////fbId: function () {
  ////  return this.get('fbData') ? this.get('fbData').id : ""
  ////}.property("fbData"),
  ////fbName: function () {
  ////  return this.get('fbData') ? this.get('fbData').name : ""
  ////}.property("fbData"),
  //fbRecord: function () {
  //  var fbId = this.get('fbId');
  //  if (!fbId) return;
  //  var fbName = this.get('fbName');
  //  this.set("application.fbName", fbName);
  //  var record = this.store.peekRecord('user', fbId);
  //  if (!record) {
  //    record = this.store.createRecord("user", {
  //      id: fbId,
  //      name: fbName,
  //      photo: `http://graph.facebook.com/${fbId}/picture?type=square`,
  //      specialties: "",
  //      preferences: ""
  //    });
  //    record.save();
  //  }
  //  return record;
  //}.observes('fbData')
});
