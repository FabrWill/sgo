import LandingModule from "./modules/landing/landing.module";
import ScheduleModule from "./modules/services/schedule.module";


const Modules = [
    ...LandingModule,
    ...ScheduleModule,
];

export default Modules;