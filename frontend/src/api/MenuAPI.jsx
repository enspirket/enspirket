import React, { useState, useEffect } from "react";

async function getMenuItems() {
    let urlPrefix = import.meta.env.VITE_URL_PREFIX
    let apiLink = `${urlPrefix}` + "/api/menu"

    try {
        const response = await fetch(apiLink, {
            method: "GET"
        })
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json()
        return data;
    }
    catch (error) {
        console.error("Error when fetching menu items.")
    }
}

export default getMenuItems