import React from 'react'
import PuffLoader from "react-spinners/PuffLoader";
export default function Loader() {
  return (
    <div className='w-full text-center flex justify-center h-screen absolute items-center'><PuffLoader
    color={"blue"}
    size={100}
    aria-label="Loading Spinner"
    data-testid="loader"
  /></div>
  )
}
