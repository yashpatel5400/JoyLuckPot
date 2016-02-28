import Mirage, {faker} from 'ember-cli-mirage';

export default Mirage.Factory.extend({
  title: (i) => `Test Potluck ${i}`,
  description: "Test",
  host: faker.name.firstName,
  lat: (i) => 37.7933 + 0.01 * i,
  lng: -122.4167,
  maxGuests: 10,
  currentGuests: 5,
  images: ["/img/61257.jpg", "/img/969189.jpg", "/img/1127678.jpg"]
});
