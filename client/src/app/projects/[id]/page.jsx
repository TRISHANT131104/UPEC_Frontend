'use client'
import { useQuery } from '@tanstack/react-query'
import { useRouter } from 'next/navigation'
import React from 'react'
import axios from 'axios'
import EachProjectCard from '@/components/ProjectPageComponents/EachProjectCard'
import WorkflowCard from '@/components/ProjectPageComponents/WorkflowCard'
import parse from 'html-react-parser';
import PRDCard from '@/components/ProjectPageComponents/PRDCard'
export default function EachProject({ params }) {
    console.log(params)
    const router = useRouter()
    console.log(router)
    const EachProject = useQuery({
        queryKey: ["EachProject"],
        queryFn: () => {
            return fetchEachProject(params.id)
        }
    })
    console.log(EachProject)
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
                        <div className="grid grid-cols-2 justify-center text-center">
                            {EachProject?.data?.workflow === null && (
                                <button className=" text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg m-5 text-center flex justify-center">Generate Workflow</button>
                            )}
                            {(EachProject?.data?.Learning_resources == null || EachProject?.data?.Learning_resources?.length == 0) && (
                                <button className=" text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg m-5 text-center flex justify-center">Generate Learning Resources</button>
                            )}
                            {(EachProject?.data?.prd != null && EachProject?.data?.project_management == null) && (
                                <button className=" text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg m-5">Generate Project Mangement</button>
                            )}


                        </div>
                    </div>

                </div>
                <div className='mx-10 my-10 text-black'>
                    <h1 className='text-center font-bold text-black my-10 text-3xl'>Workflow For Talents</h1>
                    {parse(EachProject.data ? EachProject?.data?.workflow?.description : "")}
                </div>

                <div className='mx-10 my-10 text-black'>
                    <h1 className='text-center font-bold text-black my-10 text-3xl'>Learning Resources For Talents</h1>
                    <div id="learning_resources">
                        {parse(EachProject.data ? EachProject?.data?.Learning_resources : "")}
                    </div>
                </div>

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

                <div className='mx-10 my-10 text-black'>
                    <h1 className='text-center font-bold text-black my-10 text-3xl'>Project Management</h1>
                    <div className='grid grid-cols-1 justify-center'>
                        <WorkflowCard workflowData={EachProject?.data?.project_management} />
                    {}
                    </div>
                </div>
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