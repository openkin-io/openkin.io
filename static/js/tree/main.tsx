import { createRoot } from "react-dom/client";

export const App = () => <h1>Hello World</h1>;

const root = createRoot(document.getElementById("tree")!);

root.render(<App />);
