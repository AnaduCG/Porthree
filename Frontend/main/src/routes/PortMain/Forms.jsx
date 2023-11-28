import React from 'react'
import { Link } from "react-router-dom";


function LoginForm(onClick) {
    const handleClick = (e) => {
        e.stopPropagation();
    }
    return (
        <div onClick={onClick} className="border bg-blue bg-opacity-70 py-10 px-5 absolute align-self-middle m-auto rounded-xl grid justify-center text-center gap-y-3">
            <div className="font-bold text-2xl">Porthree</div>
            <div className=""><p className="text-sm font-bold">Login to your porthree Dashboard</p></div>
            <div className="border rounded-xl font-bold flex justify-center gap-5 py-px"><div className="border rounded-full w-6 h-6"></div><button>Continue with Google</button></div>
            <div className="border rounded-xl font-bold flex justify-center gap-5 py-px"><div className="border rounded-full w-6 h-6"></div><button>Continue with Linkedin</button></div>
            <div className="flex items-center justify-center gap-2">
                <div className="border-b-4 w-1/3"></div>
                OR
                <div className="border-b-4 w-1/3"></div>
            </div>
            <div>
                <form action="" method="get" className="grid grid-cols-1 gap-2">
                    <div>
                        <input type="text" placeholder="Email or Username" className="rounded px-5 h-8 w-full outline-0" />
                    </div>
                    <div>
                        <input type="password" name="email" id="" placeholder="Password" className="rounded px-5 h-8 w-full outline-0" />
                    </div>
                    <div className="justify-self-start">
                        <label htmlFor="remember" className='font-medium'>
                            <input type="checkbox" name="remember" id="remember" />
                            Remember me?
                        </label>
                    </div>
                    <p className="font-xs">No Porthree account yet? <Link to={`/sign-up`} className="font-medium" >Sign-up</Link></p>
                    <p className="font-xs">Forgotten Porthree credentials? <a className="font-medium" href="#">recover</a></p>
                    <button type="submit" className="border rounded font-bold">Login</button>
                </form>
            </div>
        </div>
    )
}

export default function Forms({ toggleLog, handleLog }) {
    return (
        <>
            <div onClick={handleLog} className={`bg-transparent fixed flex justify-center items-center h-screen w-full  z-10 ${toggleLog ? '' : 'hidden'}`}>
                <LoginForm onClick={handleLog} />
            </div>
        </>
    )
}
