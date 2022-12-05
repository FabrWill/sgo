import React from "react";
import { TextField, TextFieldProps } from "@mui/material";
import FormikTextField from "../../types/FormikTextField";

const formatCPF = (value: string) => {
  if (!value) {
    return "";
  }

  return value
    .replace(/\D/g, "")
    .replace(/(\d{3})(\d)/, "$1.$2")
    .replace(/(\d{3})(\d)/, "$1.$2")
    .replace(/(\d{3})(\d{1,2})$/, "$1-$2");
};

const removeFomatCPF = (value: string) => {
  return value.replace(/\D+/g, "");
};

const validateCPF = (value: string) => {
  return /^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$/.test(value);
};

const CPFField: React.FC<FormikTextField & TextFieldProps> = (props) => {
  return (
    <TextField
      label="CEP"
      variant="outlined"
      sx={{ width: "100%" }}
      {...props}
      type="text"
      inputProps={{ maxLength: 14 }}
      onChange={props.formik.handleChange}
      onBlur={props.formik.handleBlur}
      onPaste={(event: any) => {
        setTimeout(() => {
          props.formik.setFieldValue(props.name, event.target.value);
        }, 150);
      }}
      value={formatCPF(props.formik.values[props.name])}
      error={
        props.formik.touched[props.name] && Boolean(props.formik.errors[props.name])
      }
      helperText={
        props.formik.touched[props.name] && (props.formik.errors[props.name] as any)
      }
    />
  );
};

export default CPFField;

export { formatCPF, removeFomatCPF, validateCPF };
