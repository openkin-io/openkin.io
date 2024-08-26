import * as PIXI from "pixi.js";

const graphics = new PIXI.Graphics();

export function tree(app: PIXI.Application) {
	app.stage.addChild(graphics);

	const depth = 11;
	const length = 200;
	const angle = Math.PI / 2;
	const delta = 1.2;
	const shortening = 0.6;
	const n = { a: 0, b: 0 };
	const mouse = {
		x: 0,
		y: 0,
	};
	const target = {
		x: 0,
		y: 0,
		vx: 0,
		vy: 0,
	};
	const k = 4;
	const f = 0.06;
	const m = 100000;

	app.stage.eventMode = "static";
	app.stage.hitArea = app.screen;

	app.stage.on("pointermove", ({ globalX, globalY }) => {
		mouse.x = globalX;
		mouse.y = globalY;
	});

	function drawTree(x: number, y: number, l: number, a: number, d: number) {
		if (d === 0 || l < 4) return;

		const endX = x + Math.cos(a) * l;
		const endY = y - Math.sin(a) * l;

		graphics
			.moveTo(x, y)
			.lineTo(endX, endY)
			.stroke({ width: d, color: 0x000000 });

		const da = n.a;
		const dl = l * n.b;

		drawTree(endX, endY, dl, a - da, d - 1);
		drawTree(endX, endY, dl, a + da, d - 1);
	}

	app.ticker.add((time) => {
		graphics.clear();
		const fx = (mouse.x - target.x) * k;
		const fy = (mouse.y - target.y) * k;
		const ax = fx / m;
		const ay = fy / m;
		target.vx += ax * time.deltaMS - target.vx * f;
		target.vy += ay * time.deltaMS - target.vy * f;
		target.x += target.vx * time.deltaMS;
		target.y += target.vy * time.deltaMS;

		const na = -0.5 + target.x / app.screen.width;
		const nb = +1.0 - target.y / app.screen.height;

		n.a = delta * na;
		n.b = shortening + nb * 0.2;

		drawTree(
			app.screen.width / 2,
			app.screen.height,
			length,
			angle - n.a / 12,
			depth,
		);
	});
}
