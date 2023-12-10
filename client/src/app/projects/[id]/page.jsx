'use client'
import { useQuery } from '@tanstack/react-query'
import { useRouter } from 'next/navigation'
import React, { useContext } from 'react'
import axios from 'axios'
import EachProjectCard from '@/components/ProjectPageComponents/EachProjectCard'
import WorkflowCard from '@/components/ProjectPageComponents/WorkflowCard'
import parse from 'html-react-parser';
import PRDCard from '@/components/ProjectPageComponents/PRDCard'
import HomeContext from '@/context/HomeContext'
export default function EachProject({ params }) {
    console.log(params)
    const { auth } = useContext(HomeContext)
    const router = useRouter()
    console.log(router)
    const EachProject = useQuery({
        queryKey: ["EachProject"],
        queryFn: () => {
            return fetchEachProject(params.id)
        }
    })

    console.log()
    
    // const CheckIfUserIsinTheProject = () =>{
    //     let members = EachProject?.data?.team?.members
    //     console.log(members)
    //     if(members.some((x)=>x.id==auth.user.id)){
    //         return true;
    //     }
    //     else{
    //         return false;
    //     }
    // }
    
    return (
        <div>
            <section className="text-gray-600 body-font">
                <div className="container mx-auto flex px-5 py-20 md:flex-row flex-col items-center">
                    <div className="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 mb-10 md:mb-0">
                        <EachProjectCard ele={EachProject?.data} />
                    </div>
                    <div className="lg:flex-grow md:w-1/2 lg:pl-24 md:pl-16 flex flex-col md:items-start md:text-left items-center text-center">
                        <h1 className="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">{EachProject?.data?.title}
                        </h1>
                        <p className="mb-8 leading-relaxed">{EachProject?.data?.description}</p>
                        {(EachProject?.data?.status != "Open" && EachProject?.data?.team?.members?.some((x)=>x.id===auth.user.id) ) && (
                            <div className="grid grid-cols-2 justify-center text-center">
                                {EachProject?.data?.workflow === null && (
                                    <button className=" text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg m-5 text-center flex justify-center items-center" onClick={() => {
                                        axios.post('http://127.0.0.1:8000/api/v1/__send__generated__workflow__/', { id: auth.user.id, project_id: EachProject?.data?.id }).then((response) => {
                                            EachProject.refetch()
                                            console.log(response.data)
                                        })
                                    }}>Generate Workflow</button>
                                )}
                                {(EachProject?.data?.Learning_resources == null || EachProject?.data?.Learning_resources?.length == 0) && (
                                    <button onClick={() => {
                                        axios.post('http://127.0.0.1:8000/api/v1/__learning__resource__/', { id: auth.user.id, project_id: EachProject?.data?.id }).then((response) => {
                                            EachProject.refetch()
                                            console.log(response.data)
                                        })
                                    }} className=" text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg m-5 text-center flex justify-center items-center">Generate Learning Resources</button>
                                )}
                                {(EachProject?.data?.prd != null && (EachProject?.data?.project_management == null || EachProject?.data?.project_management.length == 0 || EachProject?.data?.project_management == "")) && (
                                    <button onClick={() => {
                                        axios.post('http://127.0.0.1:8000/api/v1/__project__management__/', { id: auth.user.id, project_id: EachProject?.data?.id }).then((response) => {
                                            EachProject.refetch()
                                            console.log(response.data)
                                        })
                                    }} className=" text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg m-5 items-center">Generate Project Mangement</button>
                                )}


                            </div>
                        )}

                    </div>

                </div>
                {(EachProject?.data?.status != "Open" && EachProject?.data?.team?.members?.some((x)=>x.id===auth.user.id) ) && (
                    <>
                        {EachProject?.data?.workflow && (
                            <div className='mx-10 my-10 text-black'>
                                <h1 className='text-center font-bold text-black my-10 text-3xl'>Workflow For Talents</h1>
                                {EachProject.isSuccess ? parse(EachProject.data.workflow ? EachProject.data.workflow.description : "") : ""}
                            </div>
                        )}

                        {(EachProject?.data?.Learning_resources || EachProject?.data?.Learning_resources.length!=0) && (
                            <div className='mx-10 my-10 text-black'>
                                <h1 className='text-center font-bold text-black my-10 text-3xl'>Learning Resources For Talents</h1>
                                <div id="learning_resources">
                                    {EachProject.isSuccess ? parse(EachProject.data.Learning_resources ? EachProject.data.Learning_resources : "") : ""}
                                </div>
                            </div>
                        )}

                        {EachProject?.data?.prd && (
                            <div className='mx-10 my-10 text-black'>
                                <h1 className='text-center font-bold text-black my-10 text-3xl'>Project Requirement Document</h1>
                                <div className='grid grid-cols-1 justify-center'>
                                    {["project_overview", "original_requirements", "project_goals", "user_stories", "system_architecture", "tech_stacks", "requirement_pool", "ui_ux_design", "development_methodology", "security_measures", "testing_strategy", "scalability_and_performance", "deployment_plan", "maintenance_and_support", "risks_and_mitigations", "compliance_and_regulations", "budget_and_resources", "timeline_and_milestones", "communication_plan", "anything_unclear"].map((ele, index) => (
                                        <div className='my-10'>
                                            <PRDCard key={index} ele={ele} EachProject={EachProject} />
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {EachProject?.data?.project_management && (
                            <div className='mx-10 my-10 text-black'>
                                <h1 className='text-center font-bold text-black my-10 text-3xl'>Project Management</h1>
                                <div className='grid grid-cols-1 justify-center'>
                                    <WorkflowCard workflowData={EachProject?.data?.project_management} />
                                    { }
                                </div>
                            </div>
                        )}
                    </>
                )}




            </section>
            <style jsx>
                {`
                 #learning_resources  a{
                    color:blue;
                    margin:10px 10px;
                 }
                `}
            </style>
        </div>
    )
}


const fetchEachProject = async (id) => {
    return axios.get(`http://127.0.0.1:8000/api/v1/__get__each__project__/${id}`).then((response) => {
        return response.data
    }).catch((error) => {
        return []
    })
}

