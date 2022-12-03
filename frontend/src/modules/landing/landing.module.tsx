import { RouteObject } from "react-router-dom";
import ErrorPage from "../../shared/navigation/ErrorLoader";
import LandingPage from "./presenter/pages/landing.page";

const LandingModule: RouteObject[] = [
    {
        path: "/",
        element:  <LandingPage/>,
        errorElement: <ErrorPage/>,
    }
]

export default LandingModule;