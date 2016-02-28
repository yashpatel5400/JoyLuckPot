import DS from 'ember-data';

export default DS.Model.extend({
  title: DS.attr(),
  description: DS.attr(),
  time: DS.attr("date"),
  host: DS.belongsTo('user', {async: true}),
  lat: DS.attr(),
  lng: DS.attr(),
  maxGuests: DS.attr(),
  currentGuests: DS.attr(),
  attendees: DS.hasMany('attendee', {async: true}),

  imagesArray: Ember.computed("attendees.@each.imagesArray", function () {
    var images = [];
    this.get("attendees").forEach((attendee) => {
      images = images.concat(attendee.get("imagesArray"));
    });
    return images;
  })
});
