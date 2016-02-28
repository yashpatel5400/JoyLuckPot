import DS from 'ember-data';

export default DS.Model.extend({
  title: DS.attr(),
  description: DS.attr(),
  host: DS.belongsTo('user', {async: true}),
  lat: DS.attr(),
  lng: DS.attr(),
  maxGuests: DS.attr(),
  currentGuests: DS.attr(),
  images: DS.attr(),
  attendees: DS.hasMany('attendee', {async: true})
});
