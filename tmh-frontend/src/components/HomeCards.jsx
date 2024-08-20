import { Link } from 'react-router-dom';
import Card from './Card';

const HomeCards = () => {
  return (
    <section className='py-4'>
      <div className='container-xl lg:container m-auto'>
        <div className='grid grid-cols-1 md:grid-cols-2 gap-4 p-4 rounded-lg'>
          <Card bg='bg-indigo-100'>
            <h2 className='text-2xl font-bold'>Centers</h2>
            <p className='mt-2 mb-4'>
              Browse our Centers and get your care today
            </p>
            <Link
              to='/add-job'
              className='inline-block bg-indigo-500 text-white rounded-lg px-4 py-2 hover:bg-indigo-600'
            >
              Browse centers
            </Link>
          </Card>
          <Card>
            <h2 className='text-2xl font-bold'>Tests</h2>
            <p className='mt-2 mb-4'>
              List of tests provides by our centers
            </p>
            <Link
              to='/jobs'
              className='inline-block bg-black text-white rounded-lg px-4 py-2 hover:bg-gray-700'
            >
              Browse Tests
            </Link>
          </Card>

        </div>
      </div>
    </section>
  );
};
export default HomeCards;
