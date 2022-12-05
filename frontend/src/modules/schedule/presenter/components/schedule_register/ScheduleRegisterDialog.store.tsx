import { makeAutoObservable } from "mobx";
import { useFormik } from "formik";
import Schedule from "../../../domain/entities/Schedule.entity";

export class ScheduleRegisterDialogStore {
    isOpen = false;

    form = useFormik({
        initialValues: {
            ...new Schedule(),
        },
        onSubmit: this.submit,
    });

    constructor() {
        makeAutoObservable(this);
    }

    submit () {

    }

    close() {
        this.isOpen = false;
    }

    open () {
        this.isOpen = true;
    }
}