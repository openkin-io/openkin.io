import * as PIXI from "pixi.js";
import { tree } from "./fractal";
import { background } from "./background";

const app = new PIXI.Application();

const container = document.getElementById("app-container");

if (container) {
	await app.init({ background: 0xb7b7b7, resizeTo: container });

	container.appendChild(app.canvas);

	background(app);

	tree(app);
}
