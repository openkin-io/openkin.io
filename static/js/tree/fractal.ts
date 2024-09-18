import * as p from "pixi.js";

export function tree(app: p.Application) {
	const graphics = new p.Graphics();

	app.stage.addChild(graphics);

	const V = {
		// tree
		depth: 12,
		length: app.screen.height / 4,
		delta: Math.PI / 2,
		shortening: 1.5,
		// spring
		k: 15,
		f: 0.1,
		m: 1000,
		// scaling factors
		A: 0.9,
		B: 0.05,
		C: Math.PI / 16,
	};

	const n = { a: 0, b: 0, s: 0 };
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

	app.stage.eventMode = "static";
	app.stage.hitArea = app.screen;

	app.stage.on("pointermove", (event) => {
		mouse.x = event.client.x;
		mouse.y = event.client.y;
	});

	function drawTree(x: number, y: number, l: number, a: number, d: number) {
		if (d === V.depth) return;

		const endX = x + Math.cos(a) * l;
		const endY = y - Math.sin(a) * l;

		const dd = d / V.depth;

		graphics
			.moveTo(x, y)
			.lineTo(endX, endY)
			.stroke({
				width: V.depth - d,
				color: 0x111111,
				alpha: 0.4 + 0.6 * (1 - dd),
			});

		const da = n.a + V.C * (n.s * dd);
		const dl = l / n.b;

		drawTree(endX, endY, dl, a - da, d + 1);
		drawTree(endX, endY, dl, a + da, d + 1);
	}

	app.ticker.add((time) => {
		graphics.clear();
		const t = time.lastTime / 8000;
		const dt = time.deltaTime;
		const fx = (mouse.x - target.x) * V.k;
		const fy = (mouse.y - target.y) * V.k;
		const vx = (fx / V.m) * dt;
		const vy = (fy / V.m) * dt;
		target.vx += vx - target.vx * V.f;
		target.vy += vy - target.vy * V.f;
		target.x += target.vx * dt;
		target.y += target.vy * dt;

		const nx = target.x / app.screen.width;
		const ny = target.y / app.screen.height;
		const ns = Math.sin(t);

		const a = 1 - V.A + V.A * nx;
		const b = 1 - V.B + V.B * ny;

		n.a = V.delta * a;
		n.b = V.shortening * b;
		n.s = ns;

		drawTree(
			app.screen.width / 2,
			app.screen.height,
			V.length * (1 - ny) + V.length * a,
			Math.PI / 2,
			0,
		);
	});
}
