import React from "react";
import ReactDOM from "react-dom";
import "./index.css"; // Global styles
import App from "./App.js"; // Main App component

// Render the App component into the root DOM node
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
