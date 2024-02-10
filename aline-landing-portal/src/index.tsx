import React from "react";
import { createRoot } from "react-dom/client"; // Import createRoot from react-dom/client
import "./index.sass";
import App from "./App";
import reportWebVitals from "./reportWebVitals"; // Import reportWebVitals from reportWebVitals

// Use createRoot to create a root container instance
const container = document.getElementById("root"); // Get the root container
const root = createRoot(container!); // Create a root container instance

root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
