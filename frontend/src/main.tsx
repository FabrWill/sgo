import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import CssBaseline from "@mui/material/CssBaseline";

import "./core/styles/settings.css";
import "./core/styles/shortcuts.css";

import "@fontsource/raleway/latin.css";
import "@fontsource/roboto/latin.css";
import "@fontsource/inter/latin.css";
import Modules from "./modules";


const router = createBrowserRouter(Modules);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    {/* CssBaseline kickstart an elegant, consistent, and simple baseline to build upon. */}
    <CssBaseline />
    <RouterProvider router={router} />
  </React.StrictMode>
);
