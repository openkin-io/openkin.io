import * as PIXI from "pixi.js";

export function background(app: PIXI.Application) {
	const size = {
		width: app.renderer.width,
		height: app.renderer.height,
	};

	{
		const r = 16;
		const dotsContainer = new PIXI.Container();
		for (let x = r / 2; x < size.width; x += r) {
			for (let y = r / 2; y < size.height; y += r) {
				const dot = new PIXI.Graphics()
					.rect(0, 0, 2, 2)
					.fill({ color: 0, alpha: 0.1 });
				dot.position.set(x, y);
				dotsContainer.addChild(dot);
			}
		}
		app.stage.addChild(dotsContainer);
	}
}
