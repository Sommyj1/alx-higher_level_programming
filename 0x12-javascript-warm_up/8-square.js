#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
	console.log('Missing size');
} else {
	for (let i = 0; i < x: i++) {
		let y = '';
		let myVar = '';

		while (y < x) {
			myVar = myVar + 'x';
			y++;
		}
		console.log(myVar);
	}
}
