'use client'
import React from 'react'
import parse from 'html-react-parser';
export default function
    ({ ele }) {
    return (
        <div>
            <div className="flex justify-center w-full">
                <div className="max-w-full">
                    <div className="card !py-3 !px-0">
                        <div className="p-2">
                            <div className="text-md my-3 ">
                                <div><div className='grid grid-cols-[auto_auto]'>
                                    <div className="px-2 py-2 titleTextDiv">Skills Required</div>
                                    <div className='flex flex-wrap'>
                                        {ele?.related_techstacks?.map((item, index) => {
                                            return (
                                                <div key={index} className="px-2 py-2">
                                                    {item}
                                                </div>
                                            )
                                        })}
                                    </div>
                                </div>
                                    <div className='grid grid-cols-[auto_auto] '>
                                        <div className="px-2 py-2 titleTextDiv">Bid Price</div>
                                        <div className="px-2 py-2 !text-start !justify-start">{ele?.bid_price}</div>
                                    </div>
                                    <div className='grid grid-cols-[auto_auto] '>
                                        <div className="px-2 py-2 titleTextDiv">Start Date</div>
                                        <div className="px-2 py-2 !w-full !text-start !justify-start">{ele?.start_date}</div>
                                    </div>
                                    <div className='grid grid-cols-[auto_auto] '>
                                        <div className="px-2 py-2 titleTextDiv">End Date</div>
                                        <div className="px-2 py-2 !w-full !text-start !justify-start">{ele?.end_date}</div>
                                    </div>
                                    <div className='grid grid-cols-[auto_auto] '>
                                        <div className="px-2 py-2 titleTextDiv">Project Timeline</div>
                                        <div className="px-2 py-2 !w-full !text-start !justify-start">{ele?.project_timeline}</div>
                                    </div>
                                    <div className='grid grid-cols-[auto_auto] '>
                                        <div className="px-2 py-2 titleTextDiv">project status</div>
                                        <div className="px-2 py-2 !w-full !text-start !justify-start">{ele?.status}</div>
                                    </div>
                                    <div className='grid grid-cols-[auto_auto] '>
                                        <div className="px-2 py-2 titleTextDiv">Project Owner</div>
                                        <div className="px-2 py-2 !w-full !text-start !justify-start">{ele?.created_by?.user?.username}</div>
                                    </div>
                                </div></div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    )
}
