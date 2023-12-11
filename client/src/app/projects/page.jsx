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
    <div className='background'>
      
      <div className='card m-2 md:m-5 !max-lg:p-2'>
        <h1 className="headingTextDiv">Current Projects</h1>
        {CurrentProjects?.data?.length == 0 ? (
          <div className="flex flex-col items-center justify-start">
            <img src="noDataFoundGif.3a5ff8c8.gif" alt="" />
            <div className="headingTextDiv">No Projects Yet</div>
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
      <div className='card m-2 md:m-5 !max-lg:p-2'>
        <h1 className="headingTextDiv">Recommended Projects</h1>
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