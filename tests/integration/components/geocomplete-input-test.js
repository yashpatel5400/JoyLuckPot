import { moduleForComponent, test } from 'ember-qunit';
import hbs from 'htmlbars-inline-precompile';

moduleForComponent('geocomplete-input', 'Integration | Component | geocomplete input', {
  integration: true
});

test('it renders', function(assert) {
  // Set any properties with this.set('myProperty', 'value');
  // Handle any actions with this.on('myAction', function(val) { ... });"

  this.render(hbs`{{geocomplete-input}}`);

  assert.equal(this.$().text().trim(), '');

  // Template block usage:"
  this.render(hbs`
    {{#geocomplete-input}}
      template block text
    {{/geocomplete-input}}
  `);

  assert.equal(this.$().text().trim(), 'template block text');
});
