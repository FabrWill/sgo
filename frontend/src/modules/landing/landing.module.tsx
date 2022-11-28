import { RouteObject } from "react-router-dom";
import LandingPage from "./presenter/pages/landing.page";

const LandingModule: RouteObject[] = [
    {
        path: "/",
        element:  <LandingPage/>
    }
]

export default LandingModule;