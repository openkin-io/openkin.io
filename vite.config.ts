import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
	plugins: [react()],
	base: "/static/",
	// esbuild: {
	// 	jsxInject: `import React from'react'`,
	// },
	server: {
		host: "0.0.0.0",
	},

	build: {
		manifest: "manifest.json",
		emptyOutDir: true,
		rollupOptions: {
			input: {
				tree: "./static/js/tree/main.ts",
			},
		},
	},
});
