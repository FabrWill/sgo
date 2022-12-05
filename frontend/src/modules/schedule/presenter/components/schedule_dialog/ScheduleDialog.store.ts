import { makeAutoObservable } from "mobx";
import { DateTime } from "luxon";

let instance: ScheduleDialogStore;

export class ScheduleDialogStore {
    isOpen = false;

    schedule: DateTime = DateTime.now().set({minutes: 0}).setLocale("br");
    birthdate: DateTime = DateTime.now().set({minutes: 0}).setLocale("br");

    constructor() {
        makeAutoObservable(this);
    }

    changeDate(schedule: DateTime) {
        schedule.set({minute: 0});
        this.schedule = schedule;
    }

    close() {
        this.isOpen = false;
    }

    open () {
        this.isOpen = true;
    }
}

export const useScheduleStore = () => {
    if (!instance) {
        instance = new ScheduleDialogStore();
    }

    return instance;
}