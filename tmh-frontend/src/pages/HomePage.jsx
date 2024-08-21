import Hero from '../components/Hero';
import HomeCards from '../components/HomeCards';
import TestListings from '../components/TestListings';
import ViewAllHMO from '../components/ViewAllHMO';

const HomePage = () => {
  return (
    <>
      <Hero />
      <HomeCards />
      <TestListings isHome={true} />
      <ViewAllHMO />
    </>
  );
};
export default HomePage;
