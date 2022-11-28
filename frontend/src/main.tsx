import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";

import CssBaseline from "@mui/material/CssBaseline";
import { ThemeProvider } from "@mui/material/styles";

import "./core/styles/settings.css";
import "./core/styles/shortcuts.css";

import "@fontsource/raleway";

import LandingModule from "./modules/landing/landing.module";


const router = createBrowserRouter([...LandingModule]);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    {/* CssBaseline kickstart an elegant, consistent, and simple baseline to build upon. */}
    <CssBaseline />
    <RouterProvider router={router} />
  </React.StrictMode>
);
