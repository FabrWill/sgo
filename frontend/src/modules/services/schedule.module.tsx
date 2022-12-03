import { RouteObject } from "react-router-dom";
import ErrorPage from "../../shared/navigation/ErrorLoader";
import SchedulePage from "./presenter/pages/Schedule.page";

const ScheduleModule: RouteObject[] = [
    {
        path: "/home",
        element:  <SchedulePage/>,
        errorElement: <ErrorPage/>,
    }
]

export default ScheduleModule;