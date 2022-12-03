import { makeAutoObservable } from "mobx";

let instance: ScheduleDialogStore;

export class ScheduleDialogStore {
    isOpen = false;

    constructor() {
        makeAutoObservable(this);
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