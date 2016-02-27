import DS from 'ember-data';

export default DS.Model.extend({
  title: DS.attr(),
  host: DS.attr(),
  lat: DS.attr(),
  lng: DS.attr(),
  maxGuests: DS.attr(),
  currentGuests: DS.attr(),
  images: DS.attr()
});
