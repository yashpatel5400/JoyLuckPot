import Ember from 'ember';
import DS from 'ember-data';

export default DS.Model.extend({
  user: DS.belongsTo('user'),
  event: DS.belongsTo('event'),
  food: DS.attr('string'),
  images: DS.attr('string'),

  imagesArray: Ember.computed('images', function () {
    return this.get('images') ? this.get('images').split(',') : [];
  })
});
