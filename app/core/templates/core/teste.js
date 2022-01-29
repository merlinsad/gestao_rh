function sortByPriceAscending(jsonString) {

  jsonString.sort((a, b) => Number(a.price) - Number(b.price));
  console.log(jsonString);
}

console.log(sortByPriceAscending([{"name":"eggs","price":1} + {"name":"coffee","price":9.99} + {"name":"rice","price":4.04}]))
