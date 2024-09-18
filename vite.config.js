import { resolve } from "node:path";
import { defineConfig } from "vite";

export default defineConfig({
	base: "/static/",
	server: {
		host: "0.0.0.0",
	},

	build: {
		manifest: "manifest.json",
		outDir: resolve("./assets"),
		emptyOutDir: true,
		rollupOptions: {
			input: {
				tree: "./static/js/tree/main.ts",
			},
		},
	},
});
