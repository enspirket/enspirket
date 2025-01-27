import { useState, useEffect } from "react";
import getMenuItems from "../api/MenuAPI";
import MenuItem from "./MenuItem";

function Menu(){
  console.log(getMenuItems());
  return (

    

    <MenuItem 
    product_id = "D001"
    product_img = ""
    product_name_eng = "Milk Tea"
    product_name_chinese = "Milk tea"
    product_price = {4.5}
    promotion_price = {4.5}
    />
  )
}
export default Menu