#!/usr/bin/node

const person = {
    name: ["Bob", "smith"],
    age: 32,
};

function data(propertyname) {
    //console.log(person[propertyname]);
    person[propertyname][0] = "mary";
    console.log(person[propertyname]);
}

data("name");
data("age");


//console.log(person["name"][0] + " " + person.name[1])
