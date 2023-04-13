#!/usr/bin/node

const value = parseInt(process.argv[2]);

if (isNaN(value)) {
	console.log('Not anumber');
} else {
	console.log('My number: ${value}');
}
