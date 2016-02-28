import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr(),
  photo: DS.attr(),
  attendees: DS.hasMany('attendee', {async: true})
});
