import ConstellationField from "@/components/ui/constellation-field";

export default function Home() {
  return (
    <main className="relative w-full min-h-screen bg-[#070914] text-[#F2F4FB] overflow-x-hidden">
      {/* Hero with Constellation Background */}
      <section className="relative h-screen w-full flex items-center justify-center overflow-hidden">
        <ConstellationField
          mode="dark"
          speed={1}
          size={1}
          strokeWidth={1}
          length={1}
          density={1}
          opacity={1}
          className="absolute inset-0 w-full h-full -z-10"
        />

        {/* Hero Content */}
        <div className="relative z-10 max-w-5xl mx-auto w-full flex flex-col items-center text-center px-6">
          {/* Trust Indicators */}
          <div className="flex items-center gap-4 mb-12 animate-fade-in-up">
            <div className="flex -space-x-3">
              <img
                src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop"
                alt="User 1"
                className="w-12 h-12 rounded-full border border-[#1C2236] object-cover opacity-80"
              />
              <img
                src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop"
                alt="User 2"
                className="w-12 h-12 rounded-full border border-[#1C2236] object-cover opacity-80"
              />
              <img
                src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&h=100&fit=crop"
                alt="User 3"
                className="w-12 h-12 rounded-full border border-[#1C2236] object-cover opacity-80"
              />
            </div>
            <div className="flex flex-col items-start gap-1">
              <div className="flex items-center text-[#E6C879] text-lg gap-1">
                {[...Array(5)].map((_, i) => (
                  <span key={i}>★</span>
                ))}
              </div>
              <span className="text-xs font-normal uppercase text-[#9AA3BC] tracking-widest">
                Trusted by 10,000+ data teams
              </span>
            </div>
          </div>

          {/* Headline */}
          <h1 className="text-5xl md:text-7xl lg:text-8xl font-thin tracking-tight text-[#F2F4FB] text-center leading-tight max-w-5xl cursor-default mb-8">
            Uncover hidden patterns<br />with intelligent analytics
          </h1>

          {/* Subheadline */}
          <p className="mt-8 text-lg md:text-xl text-[#9AA3BC] max-w-2xl font-normal leading-relaxed mb-14">
            Synthesize complex datasets, disparate sources, and endless metrics into actionable, automated insights that guide your decisions.
          </p>

          {/* CTAs */}
          <div className="flex flex-col sm:flex-row items-center gap-6 w-full justify-center">
            <div className="p-[1px] rounded-full bg-gradient-to-br from-[#E6C879]/40 to-transparent w-full sm:w-auto shadow-2xl">
              <a
                href="#"
                className="block w-full sm:w-auto bg-[#E6C879] text-[#0E1222] px-12 py-4 rounded-full font-medium text-xs uppercase tracking-widest hover:bg-[#E6C879]/90 transition-colors"
              >
                Get Access
              </a>
            </div>

            <div className="p-[1px] rounded-full bg-gradient-to-br from-[#E6C879]/16 to-transparent w-full sm:w-auto">
              <a
                href="#"
                className="block w-full sm:w-auto bg-[#0E1222]/60 backdrop-blur-md text-[#F2F4FB] px-10 py-4 rounded-full font-medium text-xs uppercase tracking-widest hover:bg-[#1C2236]/80 transition-colors flex items-center justify-center gap-2"
              >
                Explore Demo
                <span className="text-[#7FC4FF]">→</span>
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Companies Section */}
      <section className="w-full py-20 px-6 bg-[#0E1222]/20 backdrop-blur-sm border-t border-[#1C2236]">
        <div className="max-w-6xl mx-auto">
          <p className="text-xs font-normal text-[#5C668A] mb-12 tracking-widest uppercase text-center">
            Powering data-driven enterprises
          </p>
          <div className="flex flex-wrap justify-center items-center gap-10 md:gap-16">
            {["Quantus", "NexusData", "OmniStream", "Veridian", "ApexMetrics", "Zenith"].map(
              (company) => (
                <div
                  key={company}
                  className="text-lg font-thin text-[#9AA3BC] hover:text-[#7FC4FF] hover:shadow-[0_0_12px_rgba(127,196,255,0.2)] transition-all cursor-default"
                >
                  {company}
                </div>
              )
            )}
          </div>
        </div>
      </section>
    </main>
  );
}
