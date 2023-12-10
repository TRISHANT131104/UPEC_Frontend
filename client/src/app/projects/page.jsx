'use client'
import React, { Suspense, useContext } from 'react'
import ProjectCard from '@/components/ProjectPageComponents/ProjectCard'
import HomeContext from '@/context/HomeContext'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
export default function Projects() {
  const { auth } = useContext(HomeContext)
  const AllProjects = useQuery({
    queryKey:['AllProjects'],
    queryFn:()=>{
      return fetchAllProjects()
    }
  })
  console.log(AllProjects)
  const CurrentProjects = useQuery({
    queryKey:['CurrentProjects'],
    queryFn:()=>{
      return fetchCurrentProjects(auth.user.id)
    }
  })
  return (
    <div className='bg-[#F7F7F7] text-[#D6DCE8]'>
      
      <div className='shadow-lg m-4 p-4 bg-white rounded-md'>
        <h1 className="text-lg md:text-2xl xl:text-4xl font-bold">Current Projects</h1>
        {CurrentProjects?.data?.length == 0 ? (
          <div className="flex flex-col items-center justify-start">
            <img src="noDataFoundGif.3a5ff8c8.gif" alt="" />
            <div className="font-bold text-lg md:text-xl xl:text-3xl text-[#D6DCE8]">No Projects Yet</div>
          </div>
        ) : (
          <>
            <Suspense fallback={<div>Loading...</div>}>
              {CurrentProjects?.data?.map((ele, index) => {
                return (
                  <div key={index}>
                  <ProjectCard ele={ele} />
                  </div>
                )
              })}
            </Suspense>
          </>
        )}

      </div>
      <div className='shadow-lg m-4 p-2 md:p-4 bg-white rounded-md'>
        <h1 className="text-lg md:text-2xl xl:text-4xl font-bold">Recommended Projects</h1>
        <Suspense fallback={<div>Loading...</div>}>
          {AllProjects?.data?.map((ele, index) => {
            return (
              <div key={index}>
              <ProjectCard ele={ele} />
              </div>
            )
          })}
        </Suspense>
      </div>

    </div>
  )
}



const fetchAllProjects = async (id) => {
  return axios.get(`http://127.0.0.1:8000/api/v1/__get__all__projects__`).then((response)=>{
    return response.data
  }).catch((err)=>{
    alert(err)
  })
}

const fetchCurrentProjects = async (id) => {
  return axios.get(`http://127.0.0.1:8000/api/v1/__get__users__ongoing__projects__/${id}`).then((response)=>{
    return response.data
  }).catch((err)=>{
    alert(err)
  })
}